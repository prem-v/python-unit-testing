class CloudConfig:
    def __init__(self, global_config):
        self.common_content = global_config

    def cloud_weight_by_region(self, region) -> int:
        try:
            return self.common_content[f"cc_cloud_weight_{region}"]
        except KeyError:
            return 0 # return default 0 value if not found.
    
    def cloud_enabled_by_region(self, region) -> bool:
        return self.common_content[f"cc_cloud_enabled_{region}"]
    
    def minimize_ec2_use_business_hours_by_region(self, region) -> bool:
        return self.common_content[f"cc_minimize_ec2_use_{region}_during_business_hours"]
    
    def minimize_ec2_use_after_business_hours_by_region(self, region) -> bool:
        return self.common_content[f"cc_minimize_ec2_use_{region}_after_business_hours"]