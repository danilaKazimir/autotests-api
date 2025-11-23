import grpc

from grpc_test.grpc_course import course_service_pb2
from grpc_test.grpc_course import course_service_pb2_grpc

# Устанавливаем соединение с сервером
channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

# Отправляем запрос
response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="5"))
print(response.course_id)
print(response.title)
print(response.description)
