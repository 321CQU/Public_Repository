LANUCH_PYTHON_DIR = ./course_score_query ./edu_admin_center ./mycqu_service ./notification_center
LANUCH_SWIFT_DIR = ./control_center ./cos_manager

PY_TARGET_DIR = ./target/python
SWIFT_TARGET_DIR = ./target/swift


PYTHON_SRC = $(shell find $(LANUCH_PYTHON_DIR) -name "*.proto")
SWIFT_SRC = $(shell find $(LANUCH_SWIFT_DIR) -name "*.proto")

.PHONY:launch_python

%/.:
	@mkdir -p "$@"

all: python swift

python: | $(PY_TARGET_DIR)/.
	python -m grpc_tools.protoc -I. --python_out=$(PY_TARGET_DIR) --pyi_out=$(PY_TARGET_DIR) --grpc_python_out=$(PY_TARGET_DIR) $(PYTHON_SRC)

swift: | $(SWIFT_TARGET_DIR)/.
	protoc $(SWIFT_SRC) \
    --plugin=/usr/local/bin/protoc-gen-swift \
    --swift_opt=Visibility=Public \
    --swift_out=$(SWIFT_TARGET_DIR) \
    --plugin=/usr/local/bin/protoc-gen-grpc-swift \
    --grpc-swift_opt=Visibility=Public \
    --grpc-swift_out=$(SWIFT_TARGET_DIR)