import os

project_name = input("Enter project name (i.e... project-name) : ")
os.system('docker build --tag={} .'.format(project_name))
os.system('docker run -it --entrypoint /bin/bash machinelearning')
os.system('gcloud auth login --no-launch-browser')
os.system('gcloud projects create {}'.format(project_name))
os.system('gcloud config set project {}'.format(project_name))
input('Please select "Enable Billing" at https://console.cloud.google.com/storage/browser?project={} and press enter to continue'.format(project_name))
os.system('gsutil mb gs://{}/'.format(project_name))