# Create Envfile Github Action

[![GitHub
release](https://img.shields.io/github/release/RSAWEB/create_env.svg?style=flat-square)](https://github.com/RSAWEB/create_env/releases/latest)
[![Licence](https://img.shields.io/github/license/RSAWEB/create_env)](https://github.com/RSAWEB/create_env/blob/master/LICENSE)

### RSAWEB/create_env@v1

## About

A Github Action to create a .env file with Github Secrets, limiting them to only a specified environment and format

## Usage

The Action takes the json passed in and creates a .env file limiting to <<ENVIRONMENT>>_ and starting with `[A-Z_]+=`

```yml
name: Create envfile
on: [push]
jobs:
  create_env:
    runs-on: ubuntu-18.04
    steps:
    - name: Make envfile
      uses: RSAWEB/create_env@v1
      with:
        environment: STAGING
        secrets: ${{ toJson(secrets) }}
        file_name: .env
```

## Inputs

In the example above, we use the following inputs:

| Name                      | Description                                                                                                                          |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `environment`             | The name of the environment, all secrets for this environment are prefixed with this                                                 |
| `secrets`                 | This is the JSON that we will extract the secrets from                                                                               |
| `file_name` (**Optional**) | Set the name of the output envfile. Defaults to `.env`                                                                               |

Assuming:
`environment` is `STAGING`

`secrets` is
```
{
    "STAGING_URL": "URL=http://staging.unsanctioned.co.za",
    "STAGING_KEY": "Some random key",
    "PRODUCTION_URL": "URL=https://rsaweb.co.za"
}
```

the .env file that is created from the config above would contain:

```
URL=http://staging.unsanctioned.co.za
```
