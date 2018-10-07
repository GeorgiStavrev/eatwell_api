# make sur AZUSR and AZPASS environment variables are set from secrets
export AZRG="eatwell" #resource group
export AZSUBSCR="cfa8f00c-9a83-4893-bb3b-5e594feb73de" #az subscription id
export AZACR=eatwellcr #name of container registry
export IMG_NAME=eatwell_api
export REPO_NAME=eatwell_api
export DNS_NAME=eatwell-api
export CONTAINER_NAME=eatwell-api
export TAG=v$CIRCLE_BUILD_NUM

# LOGIN to AZURE AND AZURE CONTAINER REGISTRY
az login --service-principal -u $AZUSR -p $AZPASS --tenant $AZTENANT
az account set --subscription $AZSUBSCR
az acr login --name $AZACR

# GET ACR LOGIN SERVER
export AZACR_URL=$(az acr show --name $AZACR --query loginServer | sed -e 's/^"//' -e 's/"$//')
echo "The login server is:"
echo $AZACR_URL
echo ""

# BUILD AND TAG THE IMAGE
echo "Building and pushing the image"
docker build . -t $IMG_NAME
docker tag $IMG_NAME $AZACR_URL/$REPO_NAME:$TAG
docker push $AZACR_URL/$REPO_NAME:$TAG
echo ""

# PRINT ACR CONTAINERS AND TAGS
echo "Listing repositories"
az acr repository list --name $AZACR --output table
echo ""
echo "Listing tags"
az acr repository show-tags --name $AZACR --repository $REPO_NAME --output table
echo ""

# GET ACR LOGIN SERVER
export AZACR_PASS=$(az acr credential show --name $AZACR --query "passwords[0].value" | sed -e 's/^"//' -e 's/"$//')

# DEPLOY CONTAINER
echo "Deploying container from image"
az container create --resource-group $AZRG --name $CONTAINER_NAME --image $AZACR_URL/$REPO_NAME:$TAG --cpu 1 --memory 1 --registry-login-server $AZACR_URL --registry-username $AZACR --registry-password $AZACR_PASS --dns-name-label $DNS_NAME --ports 80

# CHECK THE STATE OF THE DEPLOYMENT
echo "State of deployment:"
export DEPLOYMENT_STATE=$(az container show --resource-group $AZRG --name $CONTAINER_NAME --query instanceView.state)
echo $DEPLOYMENT_STATE
echo ""

exit $?