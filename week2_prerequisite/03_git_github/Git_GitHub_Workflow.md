# Git & GitHub Workflow

## 1. Objective

The objective of this task is to understand Git and GitHub and apply version control to the MutualFundAnalytics project.

The existing MutualFundAnalytics project is already maintained using Git and connected to a GitHub remote repository.

## 2. Repository

A Git repository is a directory where Git tracks changes to files and maintains project history.

The MutualFundAnalytics project is maintained as a Git repository.

Project structure:

MutualFundAnalytics
├── data
├── dashboard
├── notebooks
├── reports
├── scripts
├── sql
└── week2_prerequisite

## 3. Clone

Git clone is used to create a local copy of a remote GitHub repository.

Example:

```bash
git clone <repository-url>
## 12. Branch Demonstration

A separate branch named `week2-git-documentation` was created to demonstrate feature-based development.

The workflow is:

```text
master
   ↓
Create feature branch
   ↓
week2-git-documentation
   ↓
Make changes
   ↓
Commit
   ↓
Push branch
   ↓
Pull Request
   ↓
Merge into master