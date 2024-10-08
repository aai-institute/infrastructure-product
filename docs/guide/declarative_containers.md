# Declarative Environment Configuration

JobQ allows you to define your Docker environment in a declarative YAML format. Instead of writing a Dockerfile directly.

## YAML Structure

The YAML has the following structure.
```yaml
build:
  base_image: <base_image>
  dependencies:
    apt: [<apt_packages>]
    pip: [<pip_packages>]
  volumes:
    - <host_path>:<container_path>
  user:
    name: <username>
  config:
    env:
      - <env_var>: <value>
    arg:
      - <build_arg>: <value>
    stopsignal: <signal>
    shell: <shell>
  meta:
    labels:
      - <label_key>: <label_value>
  workdir: <working_directory>
  filesystem:
    copy:
      - <src>: <dest>
    add:
      - <src>: <dest>
```
Let us walk through an example of each of the options.

The YAML file uses a `build` key as the root, under which various aspects of the Docker image are defined.

First, you have to first specify the base image of the Dockerfile, for example:

```yaml
build:
  base_image: python:3.12-slim
```

Then, you can define system level and Python dependencies.

```yaml
build:
  dependencies:
    apt: [curl, git]
    pip: [attrs, pyyaml, test.whl, marker-package, -e.]
```
In order to make external storage available, you can define volume mapping. In this case, the build directory.
```yaml
build:
  volumes:
    - .:.
```
You can also define user information for running the container.
```yaml
build:
  user:
    name: no_admin
```
If applicable you can set specific configuration options such as secrets, build arguments, etc.
```yaml
build:
  config:
    env:
      - var: secret
    arg:
      - build_arg: config
    stopsignal: 1
    shell: sh
```
To control the execution environment in the container and during the build process, configure the working directory and filesystem.
```yaml
build:
  workdir: /usr/src/
  filesystem:
    copy:
      - .: .
    add:
      - .: .
```

Lastly, you can add metadata as per your convenience.
```yaml
build:
  meta:
    labels:
      - test: test
```

To use the environment specification, you have to add it in your `@job` decorator as a `spec`.
```python
from jobq.job import Job, JobOptions, ImageOptions
from pathlib import Path

job = Job(
    func=your_job_function,
    options=JobOptions(...),
    image=ImageOptions(
        spec=Path("path/to/your/docker.yaml"),
        name="your-image-name",
        tag="your-tag"
    )
)
```
jobQ will automatically generate a Dockerfile from your YAML configuration when building the image for your job.
