# HTMLtoserveusingflask

App Details:
This app is to forecast weather for next 5 days for given date. This forecasts based on average of previous years data.

It also given weather forecast for coming 5 days from third party api called Accuweather.

It used chartJS Javascript library to plot charts.

It is using api "http://ec2-3-16-181-53.us-east-2.compute.amazonaws.com/".

Used ajax calls (jquery) for for serving GET and Post requests.

Used Bootstrap 4 to place html form in a panel.

HTML hosted using python on AWS EC2 using gunicorn and nginx

Functionality:

Select some date for which you want to forecast data for the next 5 days.

You will get a forecast graph of (minimum temperature and maximum temperature) based on average from previous years data.

Other graph will show minimum temperature and maximum temperature graph of coming 5 days (Irrespective of the selected date).



