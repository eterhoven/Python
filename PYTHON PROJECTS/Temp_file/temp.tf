resource "datadog_monitor" "aws_lambda_high_error_rate" {
  evaluation_delay = "900"
  include_tags     = "true"
  message          = "[${upper(var.account)}] AWS Lambda {{functionname.name}} is above 80% error rate during the last 15 minutes. ${var.sysdev_notify_channels}"
  name             = "[${upper(var.account)}] AWS Lambda High Error Rate"
  new_group_delay  = "60"
  priority         = 2
  query            = "avg(last_15m):avg:aws.lambda.errors{aws_account:${lookup(var.account_ids, var.account, "default")},owner:sysdev} by {functionname}.as_count() / avg:aws.lambda.invocations{aws_account:${lookup(var.account_ids, var.account, "default")},owner:sysdev} by {functionname}.as_rate() * 100 > 80"

  renotify_interval   = "0"
  require_full_window = "false"

  monitor_thresholds {
    critical          = "80"
    critical_recovery = "79"
  }

  timeout_h = "0"
  type      = "query alert"
  tags      = local.aws_lambda_tags
}
