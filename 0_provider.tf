provider "aws" {
  # shared_credentials_file = "$HOME/.aws/credentials"
  access_key = var.access_key
  secret_key = var.secret_key
  region = var.region
}
