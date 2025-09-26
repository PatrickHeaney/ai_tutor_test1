# Instructions to create a new project from the `_new_prj` template, follow these steps to clone the template and set up your own local and remote repositories.

## Startup
### ✅ 1. Clone the Template Normally
First, do a standard clone of the template repository. This gives you all the files and the template's history, which we'll remove in the next step.

NOTE: This command will create a new folder named `ai_tutor_test1`.  This folder will be created inside the directory you are currently in within your terminal or command prompt.

```Bash
# Replace 'new_project_name' with your project's actual name
git clone https://github.com/PatrickHeaney/_new_prj.git ai_tutor_test1```

### ✅ 2. Navigate and Remove the Template's Git History
Move into the new directory and completely remove its .git folder. This severs the connection to the original template, leaving just the files.

```Bash
printf "\e]1;ai_tutor_test1\a"
cd ai_tutor_test1

# This command is destructive, make sure you are in the correct directory!
rm -rf .git```

### ✅ 3. Initialize a New, Fresh Repository
Now, create a brand new Git repository in the same folder. This will be the clean start for your new project and set default branch name to 'main' for consistency with GitHub

```Bash
# Initialize a new repository
git init
git branch -M main```

### ✅ 4. Stage, Commit, and Link to Your New GitHub Repo
⚠️ First, You must create a new, empty repository on GitHub to get the URL. Do this at https://github.com/new. Do not initialize it with a README or .gitignore file.

Add all the files to the new repository and make your first commit. Then, link it to the empty repository you created on GitHub.

```Bash
# Add all the files from the template
git add .

# Create the first commit for your new project's history
git commit -m "Initial commit"

# Add your new GitHub repository as the remote origin
git remote add origin https://github.com/PatrickHeaney/ai_tutor_test1.git```

### ✅ 5. Push to Your New Repository
Finally, push your new project and its clean history to GitHub.

```Bash
# Push the 'main' branch to the 'origin' remote and set it as the default
git push -u origin main```

🎉 Your new project is now successfully created with the template's files and a fresh history on your GitHub account.

## Plan

### ✅ NOTE: Start a new IDE Window, open it to your new folder named `new_project_name` and start your AI Coding asssitant now.
```Bash
Gemini```

### 1. Idea.md
✅ Update the high level descripiton of your idea in the `idea.md` file.

### 2. PLANNING.md
✅ `Read my @idea.md then read and modify the @PLANNING.md document to align with my ### Iteration 1: The Core Conversation Loop of @idea.md. Explain your modifications.`

## 3. TASK.md
✅ `Read my @idea.md and @PLANNING.md then read and modify @TASK.md document to align with my ### Iteration 1: The Core Conversation Loop of @idea.md and with @PLANNING.md. Explain your modifications.`

## 4. README.md
[] `Read my @idea.md, @PLANNING.md, and @TASK.md files, then read and modify the @README.md document to align with them. Explain your modifications.`

## Implement

### 1. Implment
[] `Implement Phase 1 of @TASK.md`

## User Test
###

## Learn
### Update  prompts
### Update update examples






# 🔥🔥🔥 OLD INSTRUCTIONS DO NOT FOLLOW
- - -
## Create a New Local Repository
Navigate into the newly cloned directory and initialize a new, non-bare repository from the bare one. This will create a fresh .git directory and the working files.

⚠️Note: You must first create an empty repository on GitHub to get the URL for YOUR_NEW_REPO_NAME. Do not include a README.md or a .gitignore when creating it on GitHub.

```Bash
cd new_project_name
git init
git remote add origin [https://github.com/YOUR_GITHUB_USERNAME/YOUR_NEW_REPO_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_NEW_REPO_NAME.git)
```

## Clean Up and Push
The new repository still has the history of the old template. To start fresh, you'll need to remove the old Git history and then add and commit your new project's files.

```Bash

# Remove old Git history
rm -rf .git

# Initialize a new git repository
git init

# Add and commit all files
git add .
git commit -m "Initial commit of new project"

# Push the new project to your GitHub repository
git push -u origin main
```

🎉🎉🎉
## These steps will give you a clean slate, with your new project code now in both your local directory and your new GitHub repository, ready for development.

# Next, Document the project
## Idea.md
[] Create a high level descripiton of your idea in the `idea.md` file.

## PLANNING.md
[] `Read my @idea.md then read and modify the @PLANNING.md document to align with my @idea.md. Explain your modifications.`

## TASK.md
[] `Read my @idea.md and @PLANNING.md then read and modify @TASK.md document to align with them. Explain your modifications`

## README.md
[] `Read my @idea.md, @PLANNING.md, and @TASK.md files, then read and modify the @README.md document to align with them. Explain your modifications.`

# Now you are on your way!!!

and can move this file to the 3_done folder.
