from grpc_tools import protoc
import os

class grpc_lib:
  proto_folder = "protos"
  output_folder = "." #relatif nya terhadap file protos bukan lokasi project atau apapun.

  def proto_to_code(self,proto_file):
      os.makedirs(self.output_folder, exist_ok=True)
      output_dir = self.output_folder
      protoc_command = f"--python_out={output_dir} --grpc_python_out={output_dir} {proto_file}"
      # Execute the protoc command
      protoc.main(protoc_command.split())

  def generate_code(self):
      for root, dirs, files in os.walk(self.proto_folder):
          for file in files:
              print(file)
              if file.endswith('.proto'):
                  proto_file = os.path.join(root, file)
                  print("Generate code for: ",proto_file)
                  self.proto_to_code(proto_file)
