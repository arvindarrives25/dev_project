# Databricks notebook source
print("This is Notebook1 with new feature")

# Set environment-specific base path
env = "dev"  # Change to "prod" in prod_project

if env == "dev":
    base_path = "/Workspace/Repos/monika_kumar5@outlook.com/dev_project"
else:
    base_path = "/Workspace/Repos/monika_kumar5@outlook.com/prod_project"

# Use base_path to call Notebook2
dbutils.notebook.run(f"{base_path}/Notebook2", timeout_seconds=600)

print("latest changes to prod")

