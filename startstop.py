
from tokenize import String

import boto3

from pprint import pprint

awsConsole = boto3.session.Session(profile_name="default")

ec2Console = awsConsole.client(service_name="ec2")


def getEC2list():
    result = ec2Console.describe_instances()['Reservations']
    #pprint(result)
    for manyInstances in result:
        for eachInstance in manyInstances['Instances']:
            pprint("Here are your instances... "+ eachInstance['InstanceId'])




pprint("which instance you want to stop?")

def stopEC2(instanceId):
    pprint("stopping the EC2")

def startEC2(instanceId):
    pprint("starting the EC2.."+instanceId)
    #ec2_client = boto3.client('ec2')
    # Start the EC2 instance
    response = ec2Console.start_instances(InstanceIds=[instanceId])
    print("ec2 start done....")
    #print(response)

def terminateEC2(instanceId):
    pprint("terminating the EC2.."+instanceId)

    # ec2_client = boto3.client('ec2')
    # Start the EC2 instance
    response = ec2Console.terminate_instances(InstanceIds=[instanceId])
    print("ec2 terminate step is  done....")
    # print(response)

def exit(instanceId):
    pprint("exiting the program...")




def main():
    print("Welcome to the stop start ops..!")
    print("Choose an operation:")
    print("1. stop ec2 instance")
    print("2. start ec2 instance")
    print("3. terminate ec2 instance")
    print("4. exit")

    #Get the user's choice
    choice = int(input("Enter the number corresponding to your choice: "))

    if choice in [1, 2, 3, 4]:
        # Perform the chosen operation
        if choice == 1:
            print("you are about to stop the EC2 instance..")
            insId = input("enter instance-id..")
            # Stop the instance
            response = ec2Console.stop_instances(InstanceIds=[insId])
            print("stopped")
        elif choice == 2:
            print("you are about to start the EC2 instance..")
            insId = input("enter instance-id..")
            # start the instance
            startEC2(insId)
            #response = ec2Console.start_insatnces(InstanceIds=[insId])
            print("done...")
        elif choice == 3:
            print("you picked number 3..")
            print(f"Welcome to terminate step..")
            insId = input("enter Instance Id..")
            print("processing....")
            print("processing....")
            print("processing....")

            terminateEC2(insId)
            print("terminated....{insId}" + insId)
        elif choice == 4:
            print(f"The result is: {exit(num1)}")






# Run the program
if __name__ == "__main__":
    getEC2list()
    main()
    getEC2list()
