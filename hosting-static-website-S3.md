# Hosting a static website in s3

## Steps to Host a Static Website on S3:

### 1. Create an S3 Bucket:
- Go to the S3 console in the AWS Management Console.
- Click Create bucket.
- `Bucket Name:` Enter a unique name for your bucket (e.g., my-static-site.com). If you plan to host the website using a domain, the bucket name should match the domain name (e.g., example.com).
- `Region:` Choose the appropriate AWS region.
- `Object Ownership:` Choose ACLs disabled (recommended) to enable bucket policies for public access.
- `Public Access Settings:` Uncheck Block all public access if you're hosting a public website (you'll be asked to confirm this).
- Leave other settings as default and click Create bucket.

### 2. Upload Website Files:
- Click on the newly created bucket.
- Click Upload to add your HTML, CSS, JavaScript, and image files. You can upload the entire folder for your static website at once.
- Ensure that the file names are accurate, with index.html being the homepage.


### 3. Enable Static Website Hosting
- In the bucket, go to the Properties tab.
Scroll down to the Static website hosting section.
- Click Edit and select Enable.
- Set the Index document to index.html and the Error document (optional) to error.html or leave it blank if you don't have one.
- Copy the Bucket website endpoint URL. This will be the URL for your website (e.g., http://my-static-site.s3-website-us-east-1.amazonaws.com).

### 4. Set Bucket Policy for Public Access
- By default, S3 buckets block public access. To allow access to your website files, you need to configure the bucket policy.
- Go to the Permissions tab of your S3 bucket.
- Click Bucket Policy and paste the following policy, replacing your-bucket-name with your bucket name:

``` json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```
- This policy allows public access to all objects in your bucket.

