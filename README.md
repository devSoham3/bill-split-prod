# BillSplit-stateless
Source code for the web application to split bills unevenly, impemented on [billsplit.sohamdeo.com](billsplit.sohamdeo.com).

## Project Structure
```
bill-split-prod
│   .dockerignore                                  --> dockeringnore for Docker build
│   .gitignore
│   app.py                                         --> Logic for operation using Flask
│   Dockerfile                                     --> Dockerfile for containerization
│   README.md
│   requirements.txt                               --> Requirements for each Docker build
│
├───static                                         --> directory to store static files needed for Flask implementation
│       style.css
│       White logo - no background no name.png
│
└───templates                                      --> directory to store HTML templates
        bill_summary.html
        enter_shares.html
        index.html
```
## Local Usage
1. Install Docker
2. Build container using: `docker build -t <container-name> .`
3. Run container using `docker run -p <localhost-port>:80 <container-name>`

## Web Applicaition
The web app is deployed via Google Cloud Run, continuous deployment is enabled with revision builds on new pushes for this repo. The build uses Dockerfile for container builds.
