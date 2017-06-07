using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JobBoardScrapers.Models
{
    // Currently, this class is just for reference and is pulled straight from the JobBoard MVC.
    // We aren't using this class here right now because we're using JSON files to push to the
    // JobBoard Azure server, but if we decide to use a DTO in C# and bypass the JSON step, then
    // this would have to replace the Dictionary<string,string> we use in the scraper.

    public class Job
    {
        public int ID { get; set; }

        [JsonProperty(PropertyName = "ApplicationLink")]
        //[Display(Name = "Application Link")]
        public string ApplicationLink { get; set; }

        [JsonProperty(PropertyName = "CompanyName")]
        //[Display(Name = "Company")]
        public string CompanyCompanyName { get; set; }

        [JsonProperty(PropertyName = "DatePosted")]
        //[Display(Name = "Date Posted")]
        public string DatePosted { get; set; }

        [JsonProperty(PropertyName = "Experience")]
        public string Experience { get; set; }

        [JsonProperty(PropertyName = "Hours")]
        public string Hours { get; set; }

        [JsonProperty(PropertyName = "JobID")]
        //[Display(Name = "Job ID")]
        public string JobID { get; set; }

        [JsonProperty(PropertyName = "JobTitle")]
        //[Display(Name = "Job Title")]
        public string JobTitle { get; set; }

        [JsonProperty(PropertyName = "LanguagesUsed")]
        //[Display(Name = "Languages Used")]
        public string LanguagesUsed { get; set; }

        [JsonProperty(PropertyName = "Location")]
        public string Location { get; set; }

        [JsonProperty(PropertyName = "Salary")]
        public string Salary { get; set; }

        //[JsonIgnore]//possible fix for api error, api can run but cannot merge jobs database with company database
        //public virtual Company Company { get; set; }


        //possible fix for api error, fully solve api
        //public Company Company { get; set; }
    }
}
