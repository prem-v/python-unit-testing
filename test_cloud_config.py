from cloud_config import CloudConfig
import unittest

class TestCloudConfig(unittest.TestCase):
  

  def test_cloud_weight_by_region(self):
    cloudConfig = CloudConfig({"cc_cloud_weight_regionName":"Test_cc_cloud_weight_regionName"})
    region = 'regionName'
    result = cloudConfig.cloud_weight_by_region(region)
    self.assertEqual(result,"Test_cc_cloud_weight_regionName")

  def test_cloud_enabled_by_region(self):
    cloudConfig = CloudConfig({"cc_cloud_enabled_regionName":"Test_cc_cloud_enabled_regionName"})
    region = 'regionName'
    result = cloudConfig.cloud_enabled_by_region(region)
    self.assertEqual(result,"Test_cc_cloud_enabled_regionName")

  def test_minimize_ec2_use_business_hours_by_region(self):
    cloudConfig = CloudConfig({"cc_minimize_ec2_use_regionName_during_business_hours":"Test_cc_minimize_ec2_use_regionName_during_business_hours"})
    region = 'regionName'
    result = cloudConfig.minimize_ec2_use_business_hours_by_region(region)
    self.assertEqual(result,"Test_cc_minimize_ec2_use_regionName_during_business_hours")
    
  def test_minimize_ec2_use_after_business_hours_by_region(self):
    cloudConfig = CloudConfig({"cc_minimize_ec2_use_regionName_after_business_hours":"Test_cc_minimize_ec2_use_regionName_after_business_hours"})
    region = 'regionName'
    result = cloudConfig.minimize_ec2_use_after_business_hours_by_region(region)
    self.assertEqual(result,"Test_cc_minimize_ec2_use_regionName_after_business_hours")
    

if __name__ == '__main__':
    unittest.main()
