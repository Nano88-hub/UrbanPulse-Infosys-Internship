# How our team works on this repo

## Golden rules

1. **Never commit a file bigger than 100 MB.** GitHub rejects it. If a dataset is
   too big, upload it to Google Drive and put the link in that milestone's README.
2. **Close the file before you commit it.** If Excel/PowerPoint/Power BI has the
   file open, Windows creates a lock file and the upload can break.
3. **One folder per milestone.** Don't invent new top-level folders.
4. **Pull before you push.** Always run `git pull` first, or you'll get a conflict.

## Where do I put my file?

| What you have | Where it goes |
|---|---|
| Raw or cleaned dataset (`.csv`, `.xlsx`) | `Milestone-N/data/` |
| Cleaning / analysis script (`.py`, `.ipynb`, `.sql`) | `Milestone-N/code/` |
| Power BI (`.pbix`) or Tableau (`.twbx`) file | `Milestone-N/dashboard/` |
| Screenshot of the dashboard (`.png`) | `Milestone-N/dashboard/` |
| The PPT you presented (`.pptx`, `.pdf`) | `Milestone-N/presentation/` |
| Written report / documentation (`.docx`, `.pdf`, `.md`) | `Milestone-N/report/` |

## The 3 commands you will use every day

```bash
git pull                        # 1. get your teammates' latest work
git add .                       # 2. stage everything you changed
git commit -m "what you did"    # 3. save it with a message
git push                        # 4. send it to GitHub
```

## Writing a good commit message

Bad: `update`, `final`, `asdf`, `new file`

Good:
- `Add Milestone 2 route preference dashboard`
- `Add weather data cleaning notebook for Milestone 1`
- `Fix null values in Bangalore traffic dataset`
