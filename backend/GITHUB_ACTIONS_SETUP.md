# GitHub Actions Setup

This project includes GitHub Actions workflows for automated testing, linting, and deployment.

## Workflows

### 1. Test and Lint (`test.yml`)
- Runs on push and pull requests to `main` and `develop` branches
- Tests against Python 3.9, 3.11, and 3.12
- Performs linting with flake8
- Runs security scanning with bandit
- Executes unit tests with pytest

### 2. Deploy to Netlify (`deploy.yml`)
- Runs on push to `main` branch
- Can be manually triggered via workflow_dispatch
- Builds the FastAPI application
- Deploys to Netlify using the Netlify Actions

### 3. Full CI/CD Pipeline (`ci.yml`)
- Comprehensive pipeline including all testing, security, and deployment steps
- Includes build artifacts and full deployment workflow

## Required Secrets

To use the deployment workflow, you need to set up the following secrets in your GitHub repository:

1. Go to your repository on GitHub
2. Navigate to Settings → Secrets and variables → Actions
3. Add the following repository secrets:

### For Netlify Deployment:
- `NETLIFY_AUTH_TOKEN`: Your Netlify personal access token
  - Get this from Netlify → User settings → Applications → Personal access tokens
- `NETLIFY_SITE_ID`: Your Netlify site ID
  - Find this in your Netlify site dashboard → Site settings → General → Site details

## Local Development

To run the same checks locally:

```bash
# Install dependencies
pip install -r requirements.txt
pip install pytest pytest-asyncio httpx flake8 bandit

# Run tests
pytest -v

# Run linting
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# Run security scan
bandit -r . -f txt
```

## Workflow Triggers

- **Push to main/develop**: Runs test and lint workflow
- **Pull requests to main/develop**: Runs test and lint workflow
- **Push to main**: Runs deployment workflow
- **Manual trigger**: Deployment workflow can be triggered manually

## Customization

You can customize the workflows by:

1. **Adding more Python versions**: Modify the `strategy.matrix.python-version` array
2. **Adding more test steps**: Add additional steps in the test job
3. **Changing deployment triggers**: Modify the `on` section of the deploy workflow
4. **Adding environment variables**: Add them to the workflow or as repository secrets

## Troubleshooting

### Common Issues:

1. **Netlify deployment fails**: Check that your secrets are correctly set
2. **Tests fail**: Ensure all dependencies are in `requirements.txt`
3. **Linting fails**: Fix code style issues or adjust flake8 configuration
4. **Security scan fails**: Review and fix security issues reported by bandit

### Getting Help:

- Check the Actions tab in your GitHub repository for detailed logs
- Review the workflow files for configuration options
- Consult the documentation for the individual actions used
