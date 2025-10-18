## 🛠️ Technical Architecture

### **Big Data Stack**
- **Apache Hadoop**: Distributed data processing framework
- **MapReduce Programming**: Python-based parallel computation
- **AWS EMR**: Cloud-native Hadoop cluster orchestration
- **Shell Script Automation**: Pipeline orchestration and job scheduling

## 🚀 Implementation & Deployment

### **Task 1: Trip Duration & Fare Analysis**
**Processing Components:**
- `Task1mapper.py`, `Task1reducer.py`, `Task1-run.sh`

**Deployment Pipeline:**
1. **Local to Jump Host Transfer**
   ```bash
   scp -i s4027264-cosc2637.pem Task1mapper.py jumphost:~/a1/
   scp -i s4027264-cosc2637.pem Task1reducer.py jumphost:~/a1/
   scp -i s4027264-cosc2637.pem Task1-run.sh jumphost:~/a1/

2. **Jump Host to EMR Master Node Deployment**
   ```bash
   scp -i ~/s4027264-cosc2637.pem Task1mapper.py hadoop@s4027264.emr.cosc2637.route53.aws.rmit.edu.au:~/
   scp -i ~/s4027264-cosc2637.pem Task1reducer.py hadoop@s4027264.emr.cosc2637.route53.aws.rmit.edu.au:~/
   scp -i ~/s4027264-cosc2637.pem Task1-run.sh hadoop@s4027264.emr.cosc2637.route53.aws.rmit.edu.au:~/

3. **Execution & Permissions**
   ```bash
   chmod +x Task1-run.sh
   ./Task1-run.sh

### **Task 2: Geospatial Clustering Analysis**
**Processing Components:**
- `Task2mapper.py`, `Task2reducer.py`, `Task2-run.sh`

**Deployment Pipeline:**
1. **Local to Jump Host Transfer**
   ```bash
   scp -i s4027264-cosc2637.pem Task2mapper.py jumphost:~/a1/
   scp -i s4027264-cosc2637.pem Task2reducer.py jumphost:~/a1/
   scp -i s4027264-cosc2637.pem Task2-run.sh jumphost:~/a1/

2. **Jump Host to EMR Master Node Deployment**
   ```bash
   scp -i ~/s4027264-cosc2637.pem Task2mapper.py hadoop@s4027264.emr.cosc2637.route53.aws.rmit.edu.au:~/
   scp -i ~/s4027264-cosc2637.pem Task2reducer.py hadoop@s4027264.emr.cosc2637.route53.aws.rmit.edu.au:~/
   scp -i ~/s4027264-cosc2637.pem Task2-run.sh hadoop@s4027264.emr.cosc2637.route53.aws.rmit.edu.au:~/

3. **Execution & Permissions**
   ```bash
   chmod +x Task2-run.sh
   ./Task2-run.sh

**Processing Components:**
- `Task1mapper.py`, `Task1reducer.py`, `Task1-run.sh`

### **Task 3: Multi-Stage Data Processing Pipeline**
**Processing Components:**
- `Task3mapper1.py`, `Task3reducer1.py` (Data Join Operation)
- `Task3mapper2.py`, `Task3reducer2.py` (Aggregation & Counting)
- `Task3mapper3.py`, `Task3reducer3.py` (Sorting & Ranking)
- `Task3-run.sh` (Pipeline Execution)

**Deployment Pipeline:**
1. **Local to Jump Host Transfer**
   ```bash
    scp -i s4027264-cosc2637.pem Task3mapper1.py jumphost:~/a1/
    scp -i s4027264-cosc2637.pem Task3mapper2.py jumphost:~/a1/
    scp -i s4027264-cosc2637.pem Task3mapper3.py jumphost:~/a1/
    scp -i s4027264-cosc2637.pem Task3reducer1.py jumphost:~/a1/
    scp -i s4027264-cosc2637.pem Task3reducer2.py jumphost:~/a1/
    scp -i s4027264-cosc2637.pem Task3reducer3.py jumphost:~/a1/
    scp -i s4027264-cosc2637.pem Task3-run.sh jumphost:~/a1/

2. **Jump Host to EMR Master Node Deployment**
   ```bash
    scp -i ~/s4027264-cosc2637.pem Task3mapper1.py hadoop@s4027264.emr.cosc2637.route53.aws.rmit.edu.au:~/
    scp -i ~/s4027264-cosc2637.pem Task3mapper2.py hadoop@s4027264.emr.cosc2637.route53.aws.rmit.edu.au:~/
    scp -i ~/s4027264-cosc2637.pem Task3mapper3.py hadoop@s4027264.emr.cosc2637.route53.aws.rmit.edu.au:~/
    scp -i ~/s4027264-cosc2637.pem Task3reducer1.py hadoop@s4027264.emr.cosc2637.route53.aws.rmit.edu.au:~/
    scp -i ~/s4027264-cosc2637.pem Task3reducer2.py hadoop@s4027264.emr.cosc2637.route53.aws.rmit.edu.au:~/
    scp -i ~/s4027264-cosc2637.pem Task3reducer3.py hadoop@s4027264.emr.cosc2637.route53.aws.rmit.edu.au:~/
    scp -i ~/s4027264-cosc2637.pem Task3-run.sh hadoop@s4027264.emr.cosc2637.route53.aws.rmit.edu.au:~/

3. **Execution & Permissions**
   ```bash
   chmod +x Task1-run.sh
   ./Task3-run.sh
