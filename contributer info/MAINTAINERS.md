# Maintainers

This document outlines the maintainers and their responsibilities for the boxedLANG project.

## Active Maintainers

### Project Owner
- **mc20000-01** - Repository owner and primary maintainer
  - Responsible for overall project direction
  - Final approval on pull requests and releases
  - Code review and quality assurance
  - Community management

## Responsibilities

### Pull Request Review
- Review code for adherence to project standards
- Verify functionality with test cases
- Request changes if needed
- Approve and merge pull requests

### Issue Management
- Triage incoming issues
- Assign labels and priorities
- Respond to questions and clarifications
- Close resolved or duplicate issues
- Plan feature work based on community needs

### Releases
- Update version numbers in `pyproject.toml`
- Update CHANGELOG.md
- Create release tags
- Publish to package repositories

### Documentation
- Maintain README accuracy
- Update guides when features change
- Review documentation pull requests
- Ensure example code works

### Community Management
- Respond to issues and discussions
- Thank contributors
- Enforce Code of Conduct
- Foster inclusive community

## Becoming a Maintainer

Contributors who have demonstrated:
- Consistent engagement and quality contributions
- Understanding of project goals and architecture
- Strong communication skills
- Commitment to community values

may be invited to become maintainers. Maintainers are expected to:
- Actively review pull requests
- Triage and respond to issues
- Maintain code quality standards
- Contribute to project planning

## Decision Making

### Major Changes
For significant changes (new language features, API changes, major refactors):

1. Open an issue with detailed proposal
2. Discuss with maintainers and community
3. Reach consensus on implementation
4. Plan implementation work
5. Submit pull request with implementation

### Minor Changes
Bug fixes, documentation updates, and small improvements can be implemented directly and submitted as pull requests.

### Release Process

1. Ensure all pull requests are merged and tested
2. Update CHANGELOG.md with all changes
3. Update version in `pyproject.toml`
4. Create a git tag: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`
5. Push tag: `git push origin vX.Y.Z`
6. Create GitHub release with changelog

## Contact and Communication

- **Issues**: [GitHub Issues](https://github.com/mc20000-01/boxedLANG-py/issues)
- **Discussions**: [GitHub Discussions](https://github.com/mc20000-01/boxedLANG-py/discussions)
- **Direct Contact**: Reach out to maintainers via GitHub

## Succession Plan

If the primary maintainer is unable to continue:

1. Active contributors will be considered for ownership
2. The project may transition to a community-maintained model
3. The GitHub repository will continue to be available
4. Community members are encouraged to create forks if needed

## Contributor Recognition

All contributors are recognized in:
- Pull request comments
- CHANGELOG.md for significant contributions
- README acknowledgments (future enhancement)

## Support and Guidance

As maintainers, we are committed to:
- Providing clear feedback on pull requests
- Helping contributors improve their submissions
- Mentoring new contributors
- Maintaining high code quality
- Keeping the project healthy and active

---

Thank you for your interest in maintaining or contributing to boxedLANG!
