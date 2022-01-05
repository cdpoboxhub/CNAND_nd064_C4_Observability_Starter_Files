**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.


MY gitrepository is https://github.com/cdpoboxhub/CNAND_nd064_C4_Observability_Starter_Files/tree/master/Project_Starter_Files-Building_a_Metrics_Dashboard


## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

See screenshot in answer-img directory.

[req1-componentsInstalled.jpg]

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

See screenshot in answer-img directory.
[req2-GrafanaLogin.jpg]

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

[req3-promethuesOnGrafana.jpg]

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

For SLO of "monthly uptime", the SLIs could be:
- The application should have 99.9% uptime during the month.

SLIs:
- Number of successful HTTP requests out of total HTTP requests should be above 99.9%
- The CPU should not be over 90% used before new pods are deployed.
- The memory should not be over 90% used before new pods are deployed.

For SLO of "request response time", the SLIs could be:
- Requests served should have a response time of 500 milliseconds 
- 



## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

Number of failed HTTP requests can be measured from keeping track of 
1. number of 40x errors returned vs 
2. 20x success codes returned. 
3. Time for succesfull span to complete from customer land on page to returned page.
4. Time for successfull span trace to complete from customer click the "correct" button
5. Time for successfull span trace to complete from customer click the "wrong" button on frontend-service webapage. 

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

Number of successfull HTTP requests fulfilled.
Time to fill an HTTP request should be below 500 milliseconds.
CPU usage percentage. To know when to deploy more pods.
Memory usage percentage. To know what threshold to deploy more pods.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
