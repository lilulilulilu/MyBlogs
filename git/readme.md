

**git删除大文件** 
```
brew install git-lfs
git lfs install
git lfs track "*.pdf"
git add .gitattributes
git commit -m "Configure Git LFS tracking"
git add your-large-file.pdf
git commit -m "Add a large file with Git LFS"

brew install git-filter-repo
#定位大文件
git rev-list --objects --all | grep $(git verify-pack -v .git/objects/pack/pack-*.idx | sort -k3nr | head)

#删除大文件并重写历史
git filter-repo --invert-paths --path "filepath" --force
git push --set-upstream https://github.com/lilulilulilu/python-notes.git main
```