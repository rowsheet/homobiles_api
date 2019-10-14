REPO_NAME=homobiles_api
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
    --env PORT="$PORT" \
    --env ROWSHEET_EMAILER_KEY="$ROWSHEET_EMAILER_KEY" \
    --env RECAPTCHA_SECRET="$RECAPTCHA_SECRET" \
    --env RECAPTCHA_MIN_SCORE="$RECAPTCHA_MIN_SCORE" \
    --publish 8006:80 \
    --name $SERVICE_NAME \
    rowsheet/$REPO_NAME:dev
