from diagrams import Diagram
from ExtendedDiagramIcons.onprem.cd.octopusDeploy import octopusDeployProgram
from ExtendedDiagramIcons.onprem.cd.octopusDeploy import octopusDeployPipeline
from ExtendedDiagramIcons.onprem.cd.octopusDeploy import octopusDeployServerNode
from ExtendedDiagramIcons.onprem.cd.octopusDeploy import octopusDeployWorkerNode
from ExtendedDiagramIcons.onprem.cd.octopusDeploy import octopusDeployWorkerPool
from ExtendedDiagramIcons.onprem.cd.octopusDeploy import octpusDeployRelease
from ExtendedDiagramIcons.generic import softwareEngineer
from ExtendedDiagramIcons.generic import JIRA
from ExtendedDiagramIcons.generic import GitHub
from ExtendedDiagramIcons.generic import ReportPortal
from ExtendedDiagramIcons.dnsProviders.namecheap import NamecheapProvider, NamecheapDomain, NamecheapAPI

def octopusDeploy_icon(val):
    return octopusDeployProgram(val)

def octopusDeployPipeline_icon(val):
    return octopusDeployPipeline(val)

def octopusDeployServerNode_icon(val):
    return octopusDeployServerNode(val)

def octopusDeployWorkerNode_icon(val):
    return octopusDeployServerNode(val)

def octopusDeployWorkerPool_icon(val):
    return octopusDeployServerNode(val)

def octpusDeployRelease_icon(val):
    return octpusDeployRelease(val)

def softwareEngineer_icon(val):
    return softwareEngineer(val)

def JIRA_icon(val):
    return JIRA(val)

def GitHub_icon(val):
    return GitHub(val)

def ReportPortal_icon(val):
    return ReportPortal(val)

def NamecheapProvider_icon(val):
    return NamecheapProvider(val)

def NamecheapDomain_icon(val):
    return NamecheapDomain(val)

def NamecheapAPI_icon(val):
    return NamecheapAPI(val)