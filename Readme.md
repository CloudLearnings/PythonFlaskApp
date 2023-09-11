## Introduction

This is a brief introduction to my project.

---

## Features

Here are some of the key features of my project.

---

## Installation

Instructions on how to install and set up my project can be found here.

---

## Usage

Learn how to use my project effectively by following these guidelines.

---

## Issues Faced
1. The base image python:3.8-slim do not have utilities such as  curl and netstat. This was faced while debugging the app
2. The container started but was not returning the http page in browser. This was due to base image by default, which bind to the port 5000 to loopback address (127.0.0.1). This was corrected by overtiding it using 

app.run(host='0.0.0.0', port=5000)


## TO DO 
add few bash script to add utilities such as curl or netstat on entrypoint or from docker file

