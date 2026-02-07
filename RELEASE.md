# Release Process

This document outlines the procedure for releasing new versions of boxedLANG.

## Release Checklist

Use this checklist to ensure a complete and professional release.

### Pre-Release (1-2 weeks before)

- [ ] Review open issues and pull requests
- [ ] Identify all changes since last release
- [ ] Plan new version number using semantic versioning
- [ ] Begin feature freeze (only critical bug fixes)
- [ ] Create a release branch if major version

### Code Preparation (Release week)

- [ ] Merge all approved pull requests
- [ ] Run comprehensive testing
  - [ ] Test all example programs
  - [ ] Verify installation process
  - [ ] Test on Python 3.8+
- [ ] Update dependencies if needed
- [ ] Review code for quality issues
- [ ] Fix any critical bugs found

### Documentation

- [ ] Update `CHANGELOG.md`:
  - [ ] Add new version section with date
  - [ ] List all added features
  - [ ] List all fixed bugs
  - [ ] List any breaking changes
  - [ ] List any deprecations
- [ ] Update `pyproject.toml` with new version number
- [ ] Update `README.md` if needed
- [ ] Verify all documentation is current
- [ ] Review ARCHITECTURE.md for accuracy
- [ ] Update DEVELOPMENT.md if process changed

### Quality Assurance

- [ ] Run existing example programs
  - [ ] `boxrun boxcode/hello.bx`
  - [ ] `boxrun boxcode/test.bx`
- [ ] Create and run new test programs
- [ ] Verify installation in clean environment:
  ```sh
  python -m venv test_env
  source test_env/bin/activate
  pip install -e .
  boxrun boxcode/hello.bx
  ```
- [ ] Check for any deprecation warnings
- [ ] Validate Python compatibility

### Git Preparation

- [ ] Ensure all changes are committed
- [ ] Verify main branch is clean:
  ```sh
  git status  # Should show no changes
  ```
- [ ] Pull latest changes from upstream
- [ ] Verify no merge conflicts

### Release Execution

**Step 1: Update Files**

```sh
# Update pyproject.toml with new version
vim pyproject.toml
# Change: version = "X.Y.Z"

# Verify version is correct
grep 'version =' pyproject.toml
```

**Step 2: Update CHANGELOG.md**

```sh
# Edit CHANGELOG.md
vim CHANGELOG.md

# Verify format is correct
```

**Step 3: Commit Changes**

```sh
# Stage changes
git add pyproject.toml CHANGELOG.md

# Create release commit
git commit -m "Release version X.Y.Z

- Added: New features list
- Fixed: Bug fixes list
- Changed: Breaking changes list"

# Verify commit
git log --oneline -5
```

**Step 4: Create Git Tag**

```sh
# Create annotated tag
git tag -a vX.Y.Z -m "Release version X.Y.Z

Release notes:
- List of major changes
- List of contributors"

# Verify tag
git tag -l -n
```

**Step 5: Push to Repository**

```sh
# Push commits
git push origin main

# Push tags
git push origin vX.Y.Z

# Verify on GitHub
# Visit https://github.com/mc20000-01/boxedLANG-py
```

**Step 6: Create GitHub Release**

1. Go to [GitHub Releases](https://github.com/mc20000-01/boxedLANG-py/releases)
2. Click "Draft a new release"
3. Select the tag you just created (vX.Y.Z)
4. Title: "boxedLANG vX.Y.Z"
5. Description: Copy from CHANGELOG.md, reformatted as:
   ```markdown
   ## What's New

   ### Added
   - Feature 1
   - Feature 2

   ### Fixed
   - Bug fix 1
   - Bug fix 2

   ### Changed
   - Change 1

   ## Contributors
   Thanks to @user1, @user2 for contributions!

   ## Checksums
   - Source code (zip)
   - Source code (tar.gz)
   ```
6. Click "Publish release"

### Post-Release

- [ ] Announce in appropriate channels
- [ ] Thank all contributors
- [ ] Review release on GitHub
- [ ] Update any external references (package registries, etc.)
- [ ] Begin next development cycle:
  ```sh
  # Create new "Unreleased" section in CHANGELOG.md
  # Update version to next dev version (e.g., 0.1.1-dev)
  ```

## Version Numbering

boxedLANG uses [Semantic Versioning](https://semver.org/):

```
MAJOR.MINOR.PATCH
  │      │      └─ Patch: Bug fixes (0.1.0 → 0.1.1)
  │      └────────── Minor: New features (0.1.0 → 0.2.0)
  └─────────────────  Major: Breaking changes (0.1.0 → 1.0.0)
```

### When to bump each version:

- **PATCH**: Bug fixes, minor improvements, documentation
- **MINOR**: New features, backward-compatible changes
- **MAJOR**: Breaking API changes, major feature releases

### Examples:

- Bug fix -> 0.1.0 to 0.1.1
- New command -> 0.1.x to 0.2.0
- Major refactor -> 0.x.x to 1.0.0

## Rollback Procedure

If a release has critical issues:

1. Delete the GitHub release
2. Delete the git tag: `git tag -d vX.Y.Z && git push origin :vX.Y.Z`
3. Identify and fix the issue
4. Create a new patch release (e.g., vX.Y.Z+1)

## Announcement Template

Use this template when announcing a new release:

```
Subject: boxedLANG vX.Y.Z Released

We're pleased to announce the release of boxedLANG vX.Y.Z!

## Highlights

- New feature 1
- New feature 2
- Bug fix 1

## Installation

pip install -U boxrun

## What's Changed

Full changelog: https://github.com/mc20000-01/boxedLANG-py/releases/tag/vX.Y.Z

## Contributing

Interested in contributing? See CONTRIBUTING.md

Thanks to all contributors!
```

## Troubleshooting

### Installation fails
- Ensure `pyproject.toml` version is updated
- Verify no syntax errors in package files
- Test installation in fresh virtual environment

### Tag already exists
```sh
# Delete local tag
git tag -d vX.Y.Z

# Delete remote tag
git push origin :vX.Y.Z

# Create new tag
git tag -a vX.Y.Z -m "Release version X.Y.Z"
```

### Need to rerevision CHANGELOG
- Make changes
- Amend commit: `git commit --amend`
- Force push: `git push -f origin main`
- Update GitHub release manually

## Emergency Release

For critical security or stability issues:

1. Create a hotfix branch
2. Implement fix with detailed commit message
3. Create pull request with `[URGENT]` prefix
4. Expedite code review
5. Merge and release as patch version
6. Document issue in CHANGELOG

## Long-term Release Planning

- Aim for at least one release per quarter
- Plan major releases 6 months in advance
- Maintain at least patches for latest two minor versions
- Consider long-term support (LTS) releases

---

For questions about the release process, ask maintainers or open an issue.
