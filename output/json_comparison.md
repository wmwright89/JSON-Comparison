# JSON Comparison

## Missing Keys

### Missing from file1
- features.enable_beta_dashboard

### Missing from file2
- database.read_replica_enabled
- features.enable_new_search
- maintenance

## Value Differences

### application

#### version
- file1_value: 2.4.1
- file2_value: 2.5.0

#### environment
- file1_value: production
- file2_value: staging

### server

#### port
- file1_value: 443
- file2_value: 8443

### database

#### host
- file1_value: db-prod-01.internal
- file2_value: db-stage-01.internal

#### pool_size
- file1_value: 20
- file2_value: 10

### authentication

#### token_expiration_minutes
- file1_value: 60
- file2_value: 45

### features

#### enable_audit_log
- file1_value: True
- file2_value: False

### logging

#### level
- file1_value: INFO
- file2_value: DEBUG

### allowed_regions
- file1_value:
  - us-east-1
  - us-west-2
  - eu-west-1
- file2_value:
  - us-east-1
  - us-west-2

### notifications

#### slack_enabled
- file1_value: False
- file2_value: True