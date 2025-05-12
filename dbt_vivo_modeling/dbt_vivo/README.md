Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices



### export env variables windows:
$env:PROJECT_ID="wissem-school"
$env:DBT_DATASET_DEV="vivo_dbt_dev" 
$env:KEYPATH_DEV="C:\Users\hp\OneDrive\Bureau\projects\SFEIR\vivo\dbt-vivo\credentials.json"
$env:LOCATION_DEV="EU"
$env:DBT_DATASET_PROD="vivo_dbt_dev"
$env:KEYPATH_PROD="C:\Users\hp\OneDrive\Bureau\projects\SFEIR\vivo\dbt-vivo\credentials.json"
$env:LOCATION_PROD="EU"
$env:DBT_TARGET="prod"


### export env variables MAC/linux:
export PROJECT_ID="wissem-school"
export DBT_DATASET_DEV="translations_dev" 
export KEYPATH_DEV="/Users/macbookair/Desktop/projects/translation/end-to-end-ELT-pipline/dbt-bigquery/credentials.json"
export LOCATION_DEV="EU"
export DBT_DATASET_PROD="translations_prod" 
export KEYPATH_PROD="/Users/macbookair/Desktop/projects/translation/end-to-end-ELT-pipline/dbt-bigquery/credentials.json"
export LOCATION_PROD="EU"
export JOB_NAME="dbt_translations_prod_marts"
export REPO_NAME="end-to-end-etl-pipline"
export LOCATION="europe-west9"
export IMAGE_TAG="latest"
export SERVICE_ACCOUNT="/app/credentials.json"



### Docker build locally:
docker build -t dbt_translations_marts .
## export variables:
# export linux/MAC: 
export $(grep -v '^#' .env | xargs)
# export windows: 
Get-Content .env | ForEach-Object {
    $name, $value = $_ -split '=', 2
    [System.Environment]::SetEnvironmentVariable($name.Trim(), $value.Trim(), [System.EnvironmentVariableTarget]::Process)
}

## running the image locally

# si tu veux charger toutes les variables en une seule commande:  
docker run --rm --env-file .env dbt_translations_marts
# Si tu veux specifier les env variables:
docker run --rm --env DBT_DATASET_DEV --env KEYPATH_DEV --env LOCATION_DEV --env PROJECT_ID dbt_translations_marts


remove docker image:
docker rmi -f dbt_translations_marts

### deploy to cloud run job:
gcloud builds submit `
    --project=$env:PROJECT_ID `
    --region=$env:LOCATION `
    --config deploy-dbt-app-cloud-run-job.yaml `
    --substitutions `
        "_PROJECT_ID=$env:PROJECT_ID,`
        _LOCATION=$env:LOCATION,`
        _REPO_NAME=$env:REPO_NAME,`
        _JOB_NAME=$env:JOB_NAME,`
        _IMAGE_TAG=$env:IMAGE_TAG,`
        _SERVICE_ACCOUNT=$env:SERVICE_ACCOUNT,`
        _DBT_DATASET_PROD=$env:DBT_DATASET_PROD,`
        _KEYPATH_DEV=$env:KEYPATH_DEV,`
        _DBT_DATASET_DEV=$env:DBT_DATASET_DEV,`
        _LOCATION_DEV=$env:LOCATION_DEV,`
        _KEYPATH_PROD=$env:KEYPATH_PROD,`
        _LOCATION_PROD=$env:LOCATION_PROD,`
        _DBT_TARGET=$env:DBT_TARGET" `
    --verbosity="debug" .


gcloud builds submit `
    --project=$env:PROJECT_ID `
    --region=$env:LOCATION `
    --config deploy-dbt-app-cloud-run-job.yaml `
    --substitutions `
        "_PROJECT_ID=$env:PROJECT_ID,`
        _LOCATION=$env:LOCATION,`
        _REPO_NAME=$env:REPO_NAME,`
        _JOB_NAME=$env:JOB_NAME,`
        _IMAGE_TAG=$env:IMAGE_TAG,`
        _SERVICE_ACCOUNT=$env:SERVICE_ACCOUNT" `
    --verbosity="debug" .

gcloud builds submit `
    --project="wissem-school" `
    --region="europe-west9" `
    --config="deploy-dbt-app-cloud-run-job.yaml" `
    --substitutions `
        _PROJECT_ID="wissem-school", `
        _LOCATION="europe-west9", `
        _REPO_NAME="end-to-end-etl-pipline", `
        _JOB_NAME="dbt_translations_prod_marts", `
        _IMAGE_TAG="latest", `
        _SERVICE_ACCOUNT="google-drive@wissem-school.iam.gserviceaccount.com" `
    --verbosity="debug" .


# run specific target
dbt run -s translation_info --target dev






