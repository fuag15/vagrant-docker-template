# Quickstart

1. `vagrant up`
2. interact with service on local port 8080

## Notes

 - the spec was vague about what to do on an existing record
   instead of raising an error or silently updating it I left a silent
   failure for now. Would have spec'd that out with all involved before 
   moving forward

 - if this were a real project it would be accompanied by unit and integration
   tests and better development workflow tools / patterns
 
 - if this were a real project there would be better logging support
   as well as configuration and argument parsing
