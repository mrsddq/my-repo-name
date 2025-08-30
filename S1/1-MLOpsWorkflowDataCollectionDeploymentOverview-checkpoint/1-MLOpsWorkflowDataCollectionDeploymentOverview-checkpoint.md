# 2-MLOpsWorkflowDataCollectionDeploymentOverview-checkpoint

high-level view of the ML life cycle
====================================

problem framing
    |
    V
data collection
    |
    V   
data transformation
    |
    V
model development, training and evaluation
    |
    V
model deployment and maintainance, monitoring

    data collection:
        oltp sources:
            OLTP (Online Transaction Processing): These are systems designed to manage transaction-oriented applications. They handle a large number of short, atomic operations such as insert, update, and delete.

        database
        csv
        parquets

        garbage in, garbage out


    data transformation:
        (1 or 0) or format

        vectorization: process via which, we breakdown the data in machine understandable format.

    model development, training and evaluation:
        in real world:
            f(input)=output
        in ml:
            (input)=output
            determine "f"

            area,rent:
            100,2500
            200,3500
            linear equation:
            y=mx+c
            rent=m(area)+c
            m=2
            c=1000
            500, rent=2(500)+1000 = 2000

