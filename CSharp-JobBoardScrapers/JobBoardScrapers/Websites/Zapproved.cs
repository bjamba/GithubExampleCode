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
    public class Zapproved
    {
        // This is the public static method to run a scheduled scrape of this website using Quartz.
        public static void Scrape(string path)
        {
            var company = "Zapproved";
            GetJobsData(company, path);
        }

        public static void GetJobsData(string company, string path)
        {
            // Creates new browser instance from which to scrape webpage.
            HtmlWeb web = new HtmlWeb();
            HtmlDocument doc = web.Load("https://careers.jobscore.com/careers/zapproved");

            // Scrapes the jobs index/splash page from which we will collect basic data.
            // This website does its postings through Jobscore.com, so the rest of the code should
            // remain the same, minus the company name.
            var websiteroot = "https://careers.jobscore.com";
            var jobTitleAndLinkArray = doc.DocumentNode.CssSelect(".js-job-title");
            var locationArray = doc.DocumentNode.CssSelect(".js-job-location");
            
            // This is a list object of dictionary objects to hold all the scraped data pre-JSON.
            List<Job> jobs = new List<Job>();

            // This loop iterates through all the instances of tags holding data to be scraped.
            for (int i = 0; i < jobTitleAndLinkArray.Count(); i++)
            {
                var titleandlink = jobTitleAndLinkArray.ElementAt(i);
                var location = locationArray.ElementAt(i);
                var job = new Job();

                job.ApplicationLink = websiteroot + titleandlink.ChildNodes[1].Attributes["href"].Value;
                job.CompanyCompanyName = company;
                job.DatePosted = DateTime.Now.ToString();
                job.Experience = "";
                job.Hours = "";
                job.JobID = "";
                job.JobTitle = System.Net.WebUtility.HtmlDecode(titleandlink.ChildNodes[1].InnerText);
                job.LanguagesUsed = "";
                job.Location = location.InnerText.Replace("\n", "");
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
