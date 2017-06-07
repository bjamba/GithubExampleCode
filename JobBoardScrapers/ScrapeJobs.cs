using System;
using Quartz;
using Quartz.Impl;
using System.Data.SqlClient;
using System.Text;
using System.Collections.Generic;
using JobBoardScrapers.Models;

namespace JobBoardScrapers
{

    class ScrapeJobs : IJob  // Labeling this "IJob" parent class is *essential* for Quartz.
    {

        static void Main(string[] args)
        {
            // 60 *60*24 seconds = 1 day.
            var intervalseconds = 5;
            ScrapeAllJobs(intervalseconds);
        }


        public static void ScrapeAllJobs(int intervalseconds)  // Schedules intervals using Quartz.
        {
            IScheduler scheduler = StdSchedulerFactory.GetDefaultScheduler();
            scheduler.Start();

            // This instantiates a "job detail" based on this website's IJob class using Quartz.
            IJobDetail job = JobBuilder.Create<ScrapeJobs>().Build();
            ITrigger trigger = TriggerBuilder.Create().
                WithDailyTimeIntervalSchedule
                (s => s
                .WithIntervalInSeconds(intervalseconds)
                .OnEveryDay()
                .StartingDailyAt(TimeOfDay.HourAndMinuteOfDay(0, 0))
                )
                .Build();

            scheduler.ScheduleJob(job, trigger);
        }


        public void Execute(IJobExecutionContext context)   // The code that gets executed on schedule.
        {
            // This is the path where JSON files will save.
            string path = @"C:\jobboardscrapes\";

            // This is where we identify each of the websites being scraped.
            Websites._10up.Scrape(path);
            Websites.Zapproved.Scrape(path);
            // Websites.Website2.Scrape(path);
            // Websites.Website3.Scrape(path);

        }

        public static void UploadScrapes(List<Job> jobs, string company)    // This connects to the DB.
        {

            try
            {
                // These are the credentials to the DB and Table where scraped data will go.
                // Remember to add a firewall exception to Azure for the IP address where this program lives on.
                SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder();
                builder.DataSource = "jobboardtestdbserver.database.windows.net";
                builder.UserID = "jobboardtestadmin";
                builder.Password = "J)Bb04rdt3st";
                builder.InitialCatalog = "jobboardtest_db";

                using (SqlConnection connection = new SqlConnection(builder.ConnectionString))
                {
                    connection.Open();
                    StringBuilder sb = new StringBuilder();

                    // This deletes all job postings from the target company from the last scrape.
                    sb.Append("DELETE FROM [dbo].[jobsTable] WHERE [CompanyName] = @CompanyName;");
                    String sql = sb.ToString();
                    using (SqlCommand command = new SqlCommand(sql, connection))
                    {
                        command.Parameters.AddWithValue("@CompanyName", company);
                        command.ExecuteNonQuery();
                    }
                    sb.Clear();


                    // This uploads all job postings from the target company from the current scrape.
                    foreach (var job in jobs)
                    {
                        sb.Append("INSERT INTO [dbo].[jobsTable] ([ApplicationLink], [CompanyName], [DatePosted], [Experience], [Hours], [JobID], [JobTitle], [LanguagesUsed], [Location], [Salary])");
                        sb.Append("VALUES (@ApplicationLink, @CompanyName, @DatePosted, @Experience, @Hours, @JobID, @JobTitle, @LanguagesUsed, @Location, @Salary);");

                        sql = sb.ToString();
                        using (SqlCommand command = new SqlCommand(sql, connection))
                        {
                            command.Parameters.AddWithValue("@ApplicationLink", job.ApplicationLink);
                            command.Parameters.AddWithValue("@CompanyName", job.CompanyCompanyName);
                            command.Parameters.AddWithValue("@DatePosted", job.DatePosted);
                            command.Parameters.AddWithValue("@Experience", job.Experience);
                            command.Parameters.AddWithValue("@Hours", job.Hours);
                            command.Parameters.AddWithValue("@JobID", job.JobID);
                            command.Parameters.AddWithValue("@JobTitle", job.JobTitle);
                            command.Parameters.AddWithValue("@LanguagesUsed", job.LanguagesUsed);
                            command.Parameters.AddWithValue("@Location", job.Location);
                            command.Parameters.AddWithValue("@Salary", job.Salary);
                            command.ExecuteNonQuery();
                        }
                        sb.Clear();
                    }

                    try
                    {
                        connection.Close();
                    }
                    catch (Exception e)
                    {
                        Console.WriteLine(e.ToString());
                    }

                    // This is just a confirmation that the job was uploaded with a timestamp.
                    Console.Write(String.Format("Jobs from {0} last uploaded on {1}.\n\n", company, DateTime.Now));
                }
            }
            catch (SqlException e)
            {
                Console.WriteLine(e.ToString());
            }

        }
    }
}
