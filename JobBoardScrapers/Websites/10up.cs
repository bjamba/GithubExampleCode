using System.Collections.Generic;
using System.Linq;
using HtmlAgilityPack;
using ScrapySharp.Extensions;
using Newtonsoft.Json;
using JobBoardScrapers.Models;
using System;
using System.Reflection;

namespace JobBoardScrapers.Websites
{
    public class _10up
    {
   
        public static void Scrape(string path)
        {
            var company = "10up";
            GetJobsData(path, company);
        }


        public static void GetJobsData(string path, string company)
        {
            // Creates new browser instance from which to scrape webpage.
            HtmlWeb web = new HtmlWeb();
            HtmlDocument doc = web.Load("https://10up.com/careers/");

            // Scrapes the jobs index/splash page from which we will collect basic data.
            var jobsArray = doc.DocumentNode.CssSelect(".tu-card");

            List<Job> jobs = new List<Job>();

            // This loop iterates through all the instances of tags holding data to be scraped.
            for (int i = 0; i < jobsArray.Count(); i++)
            {
                var item = jobsArray.ElementAt(i);
                var job = new Job();

                job.ApplicationLink = item.Attributes["href"].Value;
                job.CompanyCompanyName = company;
                job.DatePosted = DateTime.Now.ToString();
                job.Experience = "";
                job.Hours = "";
                job.JobID = "";
                job.JobTitle = System.Net.WebUtility.HtmlDecode(item.ChildNodes[0].InnerText);
                job.LanguagesUsed = "";
                job.Location = "Remote";
                job.Salary = "";

                jobs.Add(job);
            }

            //Creates a JSON file for backup.
            var json = JsonConvert.SerializeObject(jobs);
            System.IO.File.WriteAllText(path + company + ".json", json);

            ScrapeJobs.UploadScrapes(jobs, company);
            }
    }
}
