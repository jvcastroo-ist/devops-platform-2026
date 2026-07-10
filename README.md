# Athlete Performance Platform

## Thesis

A production-style observability platform for athletic performance, built to
practice a real cloud/DevOps stack end to end: containerized services,
Kubernetes, GitOps, IaC with remote state, and SRE-style observability with
real alerting.

The domain is athletic training load and sea conditions for open-water
swimming — but the point of the project is the platform underneath it.
Athlete data is simulated (this is not a personal fitness tracker); the sea
conditions data is real, pulled from a public API for the Cascais/Lisbon coast.


## Postgres

### Activities

An activitie can be divided in 3 categories, Running, Swimming and Workout.
- duration, start-time, end-time, calories, person, intensity
- distance, average pace 
