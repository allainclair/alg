## Plan

1. Analyze the requirements.
2. Make notes and design the new application/module (POC for knowledge base) based on requirements.
3. Try to organize previously some internal modules and environment (files, directories) for the application.
4. Revist crawlers and try some requests to Yelp.
5. Coding with some test cases and do the first commit. (2h window)
6. Create a "readme" instructions in how to run.
7. Plan future improvements based in the item 4.
8. Implement the improvements from item 5 (coding and testing) and do the second commit.
9. Update the "readme" instructions in how to run.

## FAQ bot

It is a core feature.

A significant portion of **conversation topics** comes from **common fact**.

topics ► request ► common facts "knowledge base" ► response to the topics.

## Challenge Notes and Requirements 

- POC knowledge base of facts.
- There is a business_list.csv with name, phone, and zip_code.
  - Some field instances are missing in phone column.
- Write a crawler to store **as much information as I can** about the business in a **structured format**.
  - Depending on how much information we get to the knowledge base, the structure can become complex. 

### Question inputs from User and implementation ideas:

1. What are the **address** and **phone number** of each business?
   1. Given the name of the business, get the street, number, city.
      Zipcode we can get from business_list.csv.
      1. Use external service for this: Yelp.
   3. Given the name of the business, get the phone number
      1. Some phone numbers are missing in the business_list.csv ->
         return a properly "Not Found Message".
      2. For the missing numbers we can use an external service
         to try to get this phone: Yelp.
         But let's not do it due to the task time limit.
2. How many businesses are registered in a given zip code (94608)?
   1. Simply count it from the business_list.csv only. it seems to be the easier requirement.
3. How many of the businesses offer wifi at their location?
   1. Use an external service to get and save this.
   2. After checking Yelp I found the "Amenities and More", but not all places have this information.
4. Which businesses serve alcohol?
   1. Use an external service to get and save this.
   2. After checking Yelp I found the "Amenities and More", but not all places have this information.
5. Let's return the "Information not found" for negatives answers of items 3. and 4.


### Decision to take about implementation

1. Let's only use the business_list.csv to limit the amount of business to answer questions as
   it is in the requirements. Other business request, we can return ► "Place not in our knowledge base".
2. Use `business_list.csv` to populate the knowledge base?
   Or just use it as a parallel source of knowledge?
   1. Populate datastore using business_list.csv:
      the request interface to the knowledge base is unified in only one datastore.
      1. It seems to get more time to implement, but it is more organized.
   2. Do not populate, we need at least two different interfaces to access the datastore:
      1. Maybe it is easier to implement at the beginning, but it can get complicated in the future due to
         request two different sources.
3. Populate an internal knowledge base from external services (Yelp)
   according to the user requests.
   1. First request populates the datastore (slow) ► following requests goes to the local database (fast).
      1. Similar to "cache".
      2. Future concerns about limiting the size of the datastore and erase old data, or to compact data.
      3. Future improvement about avoiding outdated data.

### Non functional requirements

 1. Running only local with command line interface (CLI).
 2. Let's limit the availability only for one user that run the CLI, and
    it gets the return.
 3. Future improvements:
    1. Frontend web/mobile to request a backend.

## Design

### Topology and some flows
```
              ┌───────┐           ┌─────────────┐            ┌────────────┐
         Ask  │       │  Request  │             │  Request   │            │
     ────────►│  CLI  ├──────────►│  Knowledge  ├───────────►│  External  │
User          │       │           │    Base     │            │  Service   │
     ◄────────┤       │◄──────────┤             │◄───────────┤            │
       Answer └───────┘  Response └────┬────┬───┘  Biz Info  └────────────┘
                                       │    │
                                       │    │
                                       │    │
                              Get Info │    │ Save Info
                                       ▼    ▼
                                   ┌───────────┐
                                   │           │
                                   │ Data Base │
                                   │           │
                                   └───────────┘
```

### Entities

- Business
  - Name (String)
  - Phone (String)
  - Has Wifi (Boolean)
  - Has Alcohol (Boolean)
- Address of Business
  - Number
  - Street
  - City
  - State
  - Zipcode

### Datastore model

Assuming 1:1 relationship: 1 business have only 1 address and vice-versa. But we
need more information in the address to really get it,
like adding an "apartment" attribute. I said this because we can have more business
to the same Number, Street, etc. An "apartment" number could get this model very consistent. 

Decision during implementation: first version using `.json` file.
