resource "aws_ecr_repository" "app_repo" {
  name                 = "fastapi-app"
  image_tag_mutability = "MUTABLE"
}
