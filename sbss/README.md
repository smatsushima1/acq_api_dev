# Small Business Size Standards
This API is really just the Excel sheet posted on their [website](https://www.sba.gov/document/support--table-size-standards) that lists all the size standards for a given NAICS code. I'm really not sure why this information isn't just posted as a web page due to the relatively small data size. But at least this gives me a really good reason to create an API for this for the experience.

If this was an API, the theory is that all the many end users who access this data indirectly via their contracting software will have the most accurate data for size standards. Instead of relying on many people to manually update these trivial numbers, there can be code that just reaches out and performs an API call to pull this information. The data itself isn't complex or used that much anyway, so this shouldn't be a big deal.

