#!/usr/bin/env python
# coding: utf-8

AUTHOR : SHILPA HAMPANNA NAGADI
START TIME : 11  13-05-109
END TIME   : 12:05 13-05-2019 

 Questions:
I A. What percentage of companies with a 6sense score (ss_score) of at least 85 and were added to the database (created) in January 2018 have been won(became a 6sense customer)?
        select distinct ROUND(100.0*(Select count(id) 
        from Company 
        where ss_score =85 OR  ss_score > 85
        AND create_dt BETWEEN '01-01-2019' AND '10-01-2019'
        and won = TRUE) / (select count(id) from Company) ,1)as percentage from Company;
   
B. At the company level, what is the average number of contacts that were interacted with before a successful (won) sale?
     SELECT  avg(Contact.id)
     FROM Contact
     join Company on Contact.company_id = Company.id
     join Interaction on Interaction.contact_id = Contact.id
     where won = true and interaction_dt < won_dt;

 C. What is the interaction channel and the name of BOTH the Sales rep and Customer Service rep who last interacted with the following companies: XYZ inc., ABC co., 123 ltdNote: Sales reps interact with a company through the date of a sale, while CS reps interact with a company after the date of sale.
    select Interaction.Interaction_channel ,
    (select rep_name from Interaction where rep_name  in (select rep_name 
    from Interaction join Contact on Interaction.contact_id = Contact.id
    join Company on Contact.company_id = Company.id 
    where Interaction.interaction_dt < Company.won_dt and Company.company_name in ('XYZ inc')
    ORDER BY Interaction.interaction_dt DESC limit 1))as salesrep,
              (select rep_name from Interaction where rep_name in (select  rep_name                                                 from Interaction join Contact1 on Interaction.contact_id = Contact1.id
              join Company on Contact.company_id = Company.id 
              where  Interaction.interaction_dt  > Company.won_dt and Company.company_name  in ('XYZ inc')
              ORDER BY Interaction.interaction_dt  DESC limit 1))as custrep
 from Interaction join Contact on Interaction.contact_id = Contact.id join Company on Contact.company_id = Company.id
 where Company.company_name  in ('XYZ inc')

UNION ALL

  select Interaction.Interaction_channel ,
  (select rep_name from Interaction where rep_name  in (select rep_name 
  from Interaction join Contact on Interaction.contact_id = Contact.id
   join Company on Contact.company_id = Company.id 
   where Interaction.interaction_dt < Company.won_dt and Company.company_name in ('ABC co')
   ORDER BY Interaction.interaction_dt DESC limit 1))as salesrep,
              (select rep_name from Interaction where rep_name in (select  rep_name                                                 from Interaction join Contact1 on Interaction.contact_id = Contact1.id
              join Company on Contact.company_id = Company.id 
              where  Interaction.interaction_dt  > Company.won_dt and Company.company_name  in ('ABC co')
              ORDER BY Interaction.interaction_dt  DESC limit 1))as custrep
   from Interaction join Contact on Interaction.contact_id = Contact.id join Company on Contact.company_id = Company.id
 where Company.company_name  in ('ABC co')

UNION ALL

 select Interaction.Interaction_channel ,
   (select rep_name from Interaction where rep_name  in (select rep_name 
   from Interaction join Contact on Interaction.contact_id = Contact.id
   join Company on Contact.company_id = Company.id 
   where Interaction.interaction_dt < Company.won_dt and Company.company_name in ('123 ltd')
   ORDER BY Interaction.interaction_dt DESC limit 1))as salesrep,
              (select rep_name from Interaction where rep_name in (select  rep_name                                                 from Interaction join Contact1 on Interaction.contact_id = Contact1.id
              join Company on Contact.company_id = Company.id 
              where  Interaction.interaction_dt  > Company.won_dt and Company.company_name  in ('123 ltd')
              ORDER BY Interaction.interaction_dt  DESC limit 1))as custrep
              
 from Interaction join Contact on Interaction.contact_id = Contact.id join Company on Contact.company_id = Company.id
 where Company.company_name  in ('123 ltd');


        
II. The 6sense Marketing team is planning on running a campaign in which they mail a promotional item to all prospects (individuals) that they met at a recent event, with the goal that this mailer will lead to a sales call with the prospect. The 6sense Data Science team has created a “Qualifying Model” that scores all prospects (those met at previous events, those interacted with through other channels, and those that have never been contacted) and assigns them a score (1-100 scale) predicting the likelihood that a prospect, after receiving a promotional item in the mail, will take a sales call. The Data Science team suggests that Marketing should target any prospect with a score greater than 70. How can the team test if targeting with the “Qualifying Model” score impacts the success of the campaign? Explain how you would perform this test.

Understanding :
Marketing team of the orgnisation has planned to run a promotional event in which they mail a promotional item to   all the prospects and they think would become leads
The dta science tean has come up eith a model which quqlifies all those prospects mentioned above on a scale on 1 to 100 and they propose that marketing team should focus on targeting the customers/prospects with score more than 70 as they have more liklihood of getting converted to leads.

Problem statement: 
How can the team test if targeting with the “Qualifying Model” score impacts the success of the campaign? 
Explain how you would perform this test.

Explainaitaion/Proposed Answer :
* Highly accurate estimation of promotion impact along with secondary effects needs a wise mix of machine learning algorithms 
  and coded business judgment rules. 
* The most common way to set up a lead scoring system is to use numerical values to assign a score to each lead and then  
 categorize leads into 3–4 lead buckets according to their score.
* Ideally, what i think id the  target lead score has to be correlated with 10%-15% close rates. 
  What this means is that 10%-15% of the leads that reach the Sales  team have to close in the duration of your average sales cycle.This relationship between target score and probability-to-close is important.
*Better leads mean higher conversions.
 Overall, predictive analytics(predictive modelling) allows you to make marketing campaign and other business decisions in a more informed manner. But as with other parts of life, predictive analytics doesn’t guarantee success.It merely increases the likelihood of success.

*Predictive analytics does, however, require strong understanding of “before” marketing analytics metrics to serve 
 as the foundation for modeling frameworks and scoring categories.
 After analyzing the historical and behavioral data sets and their models, you’ll be able to use them in comparison to the “before” data.

*Predictive analytics is key to successful marketing campaigns.
It integrates the correlation between metrics and better business results with advanced strategies to bring more impact across the customer life cycle.

*Once the prediction models are developed, a number of optimization use cases can be supported by plugging the models
into an optimization framework.

* To find out if this score is a realistic predictor i would recommend bootstrap sampling (also called bootstrapping)
 This method tests a model’s performance on certain subsets of data over and over again to provide an estimate of  accuracy.
 In the process you can go  back and tune parameters to simplify the model in order to improve the test performance, and then repeat the process: training and testing, training and testing.

