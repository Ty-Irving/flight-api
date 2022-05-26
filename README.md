# flight-api

## Request & Response Examples

### API Resources

  - [GET /arrivals/[airportCode]
  - [GET /departures/[airportCode]
  - [GET /enroute/[airportCode]
  - [GET /scheduled/[airportCode]
 
 ### GET/arrivals/[airportCode]
 
 Example: http://example.gov/api/v1/arrivals/[airportCode].json
 
 Response body:
  
    {
        "Ident": {
            "0": "WJA118",
            "1": "WJA2311",
            "2": "WEN3344",
          },
          
          "Type": {
            "0": "B738",
            "1": "B738",
            "2": "DH8D",
          },
          
          "From": {
            "0": "Vancouver Int'l (YVR)",
            "1": "Cancun Int'l (CUN)",
            "2": "Kelowna Int'l (YLW)",
          },
          
          "Depart": {
            "0": "16:04 PDT",
            "1": "13:51 EST",
            "2": "16:14 PDT",
          },
          
          "Arrive": {
            "0": "18:00 MDT",
            "1": "17:59 MDT",
            "2": "17:57 MDT",
          }
    }
    

 ### GET/departures/[airportCode]
 
 Example: http://example.gov/api/v1/departures/[airportCode].json
 
 Response body:
  
    {
        "Ident": {
            "0": "WJA118",
            "1": "WJA2311",
            "2": "WEN3344",
          },
          
          "Type": {
            "0": "B738",
            "1": "B738",
            "2": "DH8D",
          },
          
          "From": {
            "0": "Vancouver Int'l (YVR)",
            "1": "Cancun Int'l (CUN)",
            "2": "Kelowna Int'l (YLW)",
          },
          
          "Depart": {
            "0": "16:04 PDT",
            "1": "13:51 EST",
            "2": "16:14 PDT",
          },
          
          "Arrive": {
            "0": "18:00 MDT",
            "1": "17:59 MDT",
            "2": "17:57 MDT",
          }
    }
    
 ### GET/enroute/[airportCode]
 
 Example: http://example.gov/api/v1/enroute/[airportCode].json
 
 Response body:
  
    {
        "Ident": {
            "0": "WJA118",
            "1": "WJA2311",
            "2": "WEN3344",
          },
          
          "Type": {
            "0": "B738",
            "1": "B738",
            "2": "DH8D",
          },
          
          "From": {
            "0": "Vancouver Int'l (YVR)",
            "1": "Cancun Int'l (CUN)",
            "2": "Kelowna Int'l (YLW)",
          },
          
          "Depart": {
            "0": "16:04 PDT",
            "1": "13:51 EST",
            "2": "16:14 PDT",
          },
          
          "Arrive": {
            "0": "18:00 MDT",
            "1": "17:59 MDT",
            "2": "17:57 MDT",
          }
    }
    
    
    
 ### GET/scheduled/[airportCode]
 
 Example: http://example.gov/api/v1/scheduled/[airportCode].json
 
 Response body:
  
    {
        "Ident": {
            "0": "WJA118",
            "1": "WJA2311",
            "2": "WEN3344",
          },
          
          "Type": {
            "0": "B738",
            "1": "B738",
            "2": "DH8D",
          },
          
          "From": {
            "0": "Vancouver Int'l (YVR)",
            "1": "Cancun Int'l (CUN)",
            "2": "Kelowna Int'l (YLW)",
          },
          
          "Depart": {
            "0": "16:04 PDT",
            "1": "13:51 EST",
            "2": "16:14 PDT",
          },
          
          "Arrive": {
            "0": "18:00 MDT",
            "1": "17:59 MDT",
            "2": "17:57 MDT",
          }
    }
    
