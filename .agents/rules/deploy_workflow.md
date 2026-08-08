# Deploy Workflow Rule

When the user inputs "배포" (or requests deployment):
1. **Content Check**: Check the current conversation for any newly shared links, topics, articles, or research summaries that have not yet been saved as Markdown files in `content/post/YYYY/MM/`.
2. **Post Generation**: If unposted topics/summaries exist, automatically write high-quality Hugo Markdown post files in `content/post/YYYY/MM/` with appropriate frontmatter (title, date, categories, tags, description) and detailed content.
3. **Build & Deploy**: Execute `task deploy` to rebuild the Hugo static site (`hugo -D`), mirror `docs/` to root, commit, and push to GitHub (`gyuha.github.io`).
4. **User Response**: Provide a clean summary of the deployment with clickable Markdown links to all newly published posts on `https://gyuha.com`.
