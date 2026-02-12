# iLO RESTful API (Redfish) Interview Questions

These questions focus on the Redfish standard and HPE's implementation via the iLO RESTful API.

## 1. What is Redfish?
**Answer:** Redfish is a standard created by the DMTF (Distributed Management Task Force). It uses RESTful interfaces (HTTP/HTTPS), JSON formatting, and OData to provide a modern, secure, and scalable way to manage data center hardware. It replaces legacy IPMI.

## 2. What is the difference between Redfish and the "iLO RESTful API"?
**Answer:** Redfish is the industry standard. The iLO RESTful API is HPE's implementation of that standard, which includes the standard Redfish resources PLUS HPE-specific extensions (OEM extensions) for unique ProLiant features.

## 3. Which HTTP methods are commonly used in Redfish?
**Answer:**
- **GET:** Retrieve information (e.g., Get power status).
- **PATCH:** Modify an existing resource (e.g., Change a BIOS setting).
- **POST:** Create a new resource or perform an action (e.g., Log in, Reset server).
- **PUT:** Replace a resource (Rarely used in Redfish; PATCH is preferred).
- **DELETE:** Remove a resource (e.g., Log out/Delete session).

## 4. How do you authenticate with iLO via Redfish?
**Answer:**
1. **Basic Auth:** Send username/password in every request header (Less secure).
2. **Session-Based Auth:** `POST` credentials to `/redfish/v1/SessionService/Sessions/`. iLO returns an `X-Auth-Token` in the header. Use this token for subsequent requests.

## 5. What are "OEM Extensions" in Redfish?
**Answer:** Since Redfish is a general standard, vendors like HPE need to support unique hardware features. These are placed under the `"Oem": {"Hpe": { ... }}` property in the JSON response.

## 6. How do you find the health status of a server using Redfish?
**Answer:** Perform a `GET` on `/redfish/v1/Systems/1`. Look for the `Status` object, which typically contains `State` (e.g., "Enabled") and `Health` (e.g., "OK", "Warning", "Critical").

## 7. Explain the "Registry" concept in Redfish.
**Answer:** Registries (like the BIOS Registry) define the valid settings, types, and descriptions for a resource. Before changing a BIOS setting, an engineer should consult the registry to see if a value is a "String", "Integer", or "Enumeration."

## 8. What is the "Redfish Service Root"?
**Answer:** The entry point for the API, found at `/redfish/v1/`. It provides links to all major collections like `Systems`, `Chassis`, `Managers`, and `EthernetInterfaces`.

## 9. How do you reboot a server using Redfish?
**Answer:** Send a `POST` request to the "Reset" action URI, typically:
`/redfish/v1/Systems/1/Actions/ComputerSystem.Reset`
The body should include the reset type: `{"ResetType": "ForceRestart"}`.

## 10. What is a "Task Service" in Redfish?
**Answer:** Some operations take a long time (like firmware updates). Redfish returns a "Task" object immediately. The client can then "poll" the task URI (e.g., `/redfish/v1/TaskService/Tasks/5`) to check the progress percentage and completion status.

## 11. How do you update firmware using Redfish?
**Answer:**
1. `POST` the firmware file to `/redfish/v1/UpdateService/UpdateRepository`.
2. `POST` to `/redfish/v1/UpdateService/Actions/UpdateService.SimpleUpdate` or use the newer "Update Task" flow to schedule the installation.

## 12. Explain the "Chassis" vs "System" resource.
**Answer:** 
- **System:** Represents the logical view (CPU, RAM, OS perspective).
- **Chassis:** Represents the physical view (Sheet metal, fans, power supplies, thermal sensors).

## 13. What is "OData" (Open Data Protocol)?
**Answer:** Redfish uses OData to structure the API. Key features include `@odata.id` (the URI of the resource) and `@odata.type` (the schema version of the resource).

## 14. How do you handle "ETags" (Entity Tags) in Redfish?
**Answer:** ETags are used for concurrency control. If you `PATCH` a resource, you include the ETag in the `If-Match` header. If the resource has changed since you last read it, iLO will reject your update with a `412 Precondition Failed` error.

## 15. What are the common HTTP status codes in Redfish?
**Answer:**
- `200 OK`: Success.
- `201 Created`: Session created.
- `204 No Content`: Success (e.g., after DELETE).
- `400 Bad Request`: Invalid JSON or invalid setting.
- `401 Unauthorized`: Bad credentials.
- `404 Not Found`: URI doesn't exist.

## 16. How do you retrieve the iLO Event Log (IEL) via Redfish?
**Answer:** `GET` from `/redfish/v1/Managers/1/LogServices/IEL/Entries`.

## 17. What is the "iLOREST" or "python-ilorest-library"?
**Answer:** A Python library developed by HPE that simplifies Redfish interactions. It handles session management, error handling, and provides high-level functions so engineers don't have to write raw HTTP requests.

## 18. How do you configure a RAID array using Redfish?
**Answer:** Use the "Smart Storage" OEM extension under `/redfish/v1/Systems/1/SmartStorage`. You define a "Logical Drive" object and `POST` it to the controller's configuration service.

## 19. What is "Schema" in Redfish?
**Answer:** The CSDL (XML) or JSON Schema files that define the structure of a Redfish resource. They are used to validate that an API response is compliant with the standard.

## 20. How would you use Redfish to detect an ARM-based server?
**Answer:** `GET` on `/redfish/v1/Systems/1`. Check the `ProcessorSummary` or individual `Processors` members. Look for `Architecture` or the `InstructionSet` property which will indicate `ARM-64` instead of `x86-64`.
