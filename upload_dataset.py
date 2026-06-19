from huggingface_hub import HfApi

api = HfApi()

# Create dataset repo
api.create_repo(
    repo_id="unicorn-s/nepal-border-sentiment-dataset",
    repo_type="dataset",
    private=False
)

# Upload CSV files
api.upload_file(
    path_or_fileobj="nepal_border_comments.csv",
    path_in_repo="nepal_border_comments.csv",
    repo_id="unicorn-s/nepal-border-sentiment-dataset",
    repo_type="dataset"
)

api.upload_file(
    path_or_fileobj="nepal_comments_labelled.csv",
    path_in_repo="nepal_comments_labelled.csv",
    repo_id="unicorn-s/nepal-border-sentiment-dataset",
    repo_type="dataset"
)

api.upload_file(
    path_or_fileobj="comments_manual_review.csv",
    path_in_repo="comments_manual_review.csv",
    repo_id="unicorn-s/nepal-border-sentiment-dataset",
    repo_type="dataset"
)
