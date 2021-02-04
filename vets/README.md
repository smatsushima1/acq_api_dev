# VETS-4212 Registrations
Perhaps the smallest in scale of all these projects, this API will actually not even be an API at all since there already is one that exists for SAM Entity Registration information. My goals for this are quite simple:

- [ ] Download the VETS data
- [ ] Move al the data into a json file
- [ ] Join the fields based on company name and address to get their CAGE and DUNS numbers
  - This step is ridiculous: why not include these crucial codes in your report in the first place?
- [ ] Save the new dataset with the updated CAGE and DUNS codes

On a high level, this information will at least provide some guidance to the SAM Entity Registration folks who currently don't have a way of identifying whether their entities have registered in SAM. Including this information will at least prevent a large majority of Contract Administrators from checking an Excel file every time they exercise an option, assuming the Contractor is required to have been registered.

A simple Boolean 'Yes', 'No', 'Not Required' answer will all that will be needed to supplement the currently existing API to make it that much more helpful.

