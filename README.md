# hadoop related settings and practices

+ VMware-Virtual Mechine
  + version: CentOS-7-x86_64-DVD-2009
  + link: https://www.centos.org/download/
  + settings(file): vmware(for network); input/bash_profile(environment variables for hadoop and jdk)
+ JDK
  + version: jdk-8u191-linux-x64
  + link: https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html
+ Hadoop
  + version: hadoop-3.3.2
  + link:https://dlcdn.apache.org/hadoop/common/
  + settings(file): input; online tuturial(https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html#YARN_on_a_Single_Node)
  + practices: verify-cases
+ Warning
  + the version of JDK should not be larger than 8.

# hive
+ requirement: installed JDK and Hadoop
+ mysql on docker
  + install docker and create mysql container
+ setting(file): hive(including updated bash_profile and inputs)

# sqoop
+ link: https://archive.apache.org/dist/sqoop
+ warning: put file of "common-lang-2.6.jar" under $SQOOP_HOME/lib
+ common-lang-2.6.jar: https://mvnrepository.com/artifact/commons-lang/commons-lang/2.6

# HBase
+ link: https://archive.apache.org/dist/hbase/
+ settings (file): hbasetmp

