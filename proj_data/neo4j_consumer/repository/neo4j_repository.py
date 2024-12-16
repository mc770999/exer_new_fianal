from proj_data.neo4j_consumer.database import driver


def create_nodes(nodes_data):
    with driver.session() as session:
        query = """
                UNWIND $data AS row
                MERGE (n1:Student {student_id: row.student_id})
                MERGE (n2:Teacher {teacher_id: row.teacher_id})
                MERGE (n3:Class {class_id: row.class_id})
                MERGE (n1)-[:ENROLLED_IN]->(n3)<-[:ENROLLED_IN]-(n2)
                RETURN n1, n2, n3
                """
        params = {
            'data': nodes_data
        }
        res = session.run(query, params).data()
        return  next((r for r in res),{}).get("n", {})