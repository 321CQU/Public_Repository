BASE_DIR = ./micro_services_protobuf
LAUNCH_PYTHON_DIR = course_score_query edu_admin_center mycqu_service notification_center control_center
LAUNCH_SWIFT_DIR = control_center cos_manager

ADDITIONAL_FILE = common.proto

PY_TARGET_DIR = ./proto_build/python
SWIFT_TARGET_DIR = ./proto_build/swift


PYTHON_SRC = $(shell find $(foreach dir, $(LAUNCH_PYTHON_DIR), $(BASE_DIR)/$(dir) ) -name "*.proto") $(BASE_DIR)/$(ADDITIONAL_FILE)
SWIFT_SRC = $(shell find $(foreach dir, $(LAUNCH_SWIFT_DIR), $(BASE_DIR)/$(dir) ) -name "*.proto" ) $(BASE_DIR)/$(ADDITIONAL_FILE)

.PHONY:clean

%/.:
	@mkdir -p "$@"

all: python swift

python: | $(PY_TARGET_DIR)/.
	python -m grpc_tools.protoc -I. --python_out=$(PY_TARGET_DIR) --pyi_out=$(PY_TARGET_DIR) --grpc_python_out=$(PY_TARGET_DIR) \
	$(PYTHON_SRC)
	find $(PY_TARGET_DIR) -type d -exec touch {}/__init__.py \;
	rm -f $(PY_TARGET_DIR)/__init__.py;

swift: | $(SWIFT_TARGET_DIR)/.
	protoc $(SWIFT_SRC) \
    --plugin=/usr/local/bin/protoc-gen-swift \
    --swift_opt=Visibility=Public \
    --swift_out=$(SWIFT_TARGET_DIR) \
    --plugin=/usr/local/bin/protoc-gen-grpc-swift \
    --grpc-swift_opt=Visibility=Public \
    --grpc-swift_out=$(SWIFT_TARGET_DIR);