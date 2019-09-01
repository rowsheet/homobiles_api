REPO_NAME=rowsheet_emailer
SERVICE_NAME=dev--$REPO_NAME
echo REPO_NAME:$REPO_NAME
echo SERVICE_NAME:$SERVICE_NAME
#-------------------------------------------------------------------------------
# Remove the old service.
#-------------------------------------------------------------------------------
docker service rm $SERVICE_NAME

#-------------------------------------------------------------------------------
# Build the new image.
#-------------------------------------------------------------------------------
docker build -t rowsheet/$REPO_NAME:dev .

#-------------------------------------------------------------------------------
# Source credentials.
#-------------------------------------------------------------------------------
source ./creds

docker service create \
    --env CREDENTIALS_DOT_JSON="$CREDENTIALS_DOT_JSON" \
    --env CREDENTIALS_DOT_TOKEN_DOT_B64="$CREDENTIALS_DOT_TOKEN_DOT_B64 " \
    --publish 8004:80 \
    --name $SERVICE_NAME \
    rowsheet/$REPO_NAME:dev
