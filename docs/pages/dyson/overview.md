# Dyson Router Documentation

## Introduction

The **Dyson Router** is a cutting-edge solution designed to dynamically route computational workloads to the most optimal hardware in real-time. By leveraging advanced AI-driven hardware mapping techniques, Dyson delivers unprecedented performance and efficiency.

### Key Benefits

- **Improved Performance**: Intelligently run workloads on hardware specifically optimized for your use case
- **Cost Efficiency**: Achieve up to 20% cost savings on hardware usage
- **Future-Proofing**: Seamlessly adapt as new hardware options emerge
- **Resilience**: Automatically reroute workloads away from underperforming or degraded hardware

## How Dyson Works

Dyson revolutionizes hardware routing through a sophisticated three-step approach:

1. **Hardware Profiling**
   - Builds comprehensive performance profiles for each available hardware option
   - Ensures routing decisions are based on in-depth, data-driven analysis

2. **Dynamic Workload Routing**
   - Evaluates each request comprehensively
   - Routes to the hardware configuration most suited to its unique requirements

3. **Continuous Optimization**
   - Monitors performance in real-time
   - Adapts dynamically to changing computational conditions
   - Guarantees consistently efficient workload execution


## Advanced Routing Parameters

| Parameter     | Description                                                                               | Default Value | Possible Values                 |
|--------------|-------------------------------------------------------------------------------------------|--------------|--------------------------------|
| `mode`       | Defines optimization criteria                                                             | `performance`| `energy-efficient`, `performance` |
| `judge`      | Number of LLMs used to determine hardware suitability                                     | `1`          | Integer (1-5)                  |
| `run_type`   | Specifies execution log type                                                              | `minimal`    | `log`, `minimal`, `detailed`   |
| `complexity` | Indicates task complexity level                                                           | `low`        | `low`, `medium`, `high`        |
| `precision`  | Defines required precision level                                                          | `normal`     | `low`, `normal`, `high`        |
| `multi_device`| Enables routing across multiple devices                                                   | `False`      | `True`, `False`                |


## Best Practices

1. Always securely manage your API key
2. Start with lower complexity and precision settings
3. Monitor initial routing results
4. Gradually increase `judge` parameter for more refined hardware selection
5. Utilize `multi_device` for complex, resource-intensive workloads

## Support

For additional support, contact Dyson technical support support@crossgl.net.