# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

export JAVA_HOME="/root/hadoop/app/jdk1.8.0_191"
export PATH=$JAVA_HOME/bin:$PATH

export HADOOP_HOME="/root/hadoop/app/hadoop-3.3.2"
export PATH=$HADOOP_HOME/bin:$PATH

export HIVE_HOME="/root/hadoop/app/apache-hive-2.3.8-bin"
export PATH=$HIVE_HOME/bin:$PATH

PATH=$PATH:$HOME/bin

export PATH
