import os

import pytest
import shutil

import definitions
from scripts import workflow

TEST_DIR = definitions.TESTS_DIR / 'scripts' / 'workflow'


class TestExpandWorkflow:
    def test_null_version(self):
        workflow_path = definitions.SUBWORKFLOWS_DIR / 'generation' / 'madgraph_pythia' / 'madgraph.yml'
        actual = workflow.expand_workflow(workflow_path, workflow_path)
        print(actual)

    def test_simple(self):
        workflow_path = definitions.SUBWORKFLOWS_DIR / 'selection' / 'rivet' / 'workflow.yml'
        toplevel_path = workflow_path.parent
        actual = workflow.expand_workflow(workflow_path, toplevel_path)


class TestMakeWorkflowFromYaml:
    @pytest.mark.skip(reason="not fully implemented.")
    def test_valid_args(self):
        input_path = os.path.join(TEST_DIR, 'valid_input.yml')
        expected = {}
        actual = workflow.make_workflow_from_yaml(input_path)
        assert actual == expected


class TestMakeWorkflow:
    def test_make_subworkflow(self):
        actual = workflow.make_subworkflow('generation',
                                           'madgraph_pythia',
                                           {'pythia_version': '1.0.0', 'madgraph_version': '1.0.0'})
        print(actual)

    def test_valid_args_debug(self):
        steps = ['generation']
        names = ['madgraph_pythia']
        actual = workflow.make_workflow(steps, names, [])
        print(actual)

    # @pytest.mark.skip(reason="not fully implemented.")
    def test_valid_args(self):
        steps = ['generation', 'selection', 'statistics']
        names = ['madgraph_pythia', 'rivet', 'pyhf']
        environment_settings = [{}, {}, {}]
        actual = workflow.make_workflow(steps, names, environment_settings)
