from pathlib import Path

from phidata.workspace.settings import WorkspaceSettings

#
# -*- Define workspace settings using the WorkspaceSettings class
#
ws_settings = WorkspaceSettings(
    # Workspace name: used for naming cloud resources
    ws_name="backend",
    # Path to the workspace directory
    ws_dir=Path(__file__).parent.resolve(),
    # -*- Dev settings
    dev_env="dev",
    # -*- Dev Apps
    dev_api_enabled=True,
    dev_postgres_enabled=True,
    dev_redis_enabled=True,
    # -*- Production settings
    prd_env="prd",
    # Domain for the production platform
    prd_domain="api.phidata.com",
    # -*- Production Apps
    prd_api_enabled=True,
    prd_postgres_enabled=True,
    prd_redis_enabled=True,
    # -*- AWS settings
    # Region for AWS resources
    aws_region="us-east-1",
    # Availability Zones for AWS resources
    aws_az1="us-east-1a",
    aws_az2="us-east-1b",
    # aws_az3="us-east-1c",
    # Subnet IDs for AWS resources
    # Public subnets. 1 in each AZ.
    public_subnets=["subnet-0aebed09ea7c82a5f", "subnet-0d53d74c0bb98ac9d"],
    # Private subnets. 1 in each AZ.
    private_subnets=["subnet-0c2587701e140e69e", "subnet-0964a2e70b7289ee5"],
    # Security Groups for AWS resources
    security_groups=["sg-0cc91078ab56a5a13"],
    # -*- Image Settings
    # Repository for images
    image_repo="386435111151.dkr.ecr.us-east-1.amazonaws.com",
    # Suffix added to the image name
    image_suffix="api",
    # Build images locally
    build_images=True,
    # Push images after building
    push_images=True,
    # Skip cache when building images
    # skip_image_cache=False,
    # Force pull images in FROM
    # force_pull_images=False,
)
